import sqlmodel as sqm

import lamindb as db

from ...dev.id import id_file, id_user  # noqa
from . import get_engine


class insert_if_not_exists:
    """Insert data if it does not yet exist."""

    @classmethod
    def user(cls, user_name):
        df_user = db.do.load("user")

        if user_name in df_user.name.values:
            user_id = df_user.index[df_user.name == user_name][0]
            print(f"user {user_name} ({user_id}) already exists")
        else:
            user_id = insert.user(user_name)  # type: ignore
            print(f"added user {user_name} ({user_id})")

        return user_id


class insert:
    """Insert data."""

    @classmethod
    def user(cls, user_name):
        """User."""
        engine = get_engine()

        with sqm.Session(engine) as session:
            user = db.model.user(name=user_name)
            session.add(user)
            session.commit()
            session.refresh(user)

        return user.id

    @classmethod
    def file(cls, name: str, *, interface: str = None, interface_name: str = None):
        """Data file with its origin."""
        interface_id = interface
        engine = get_engine()

        if interface_id is None:
            from nbproject import meta

            interface_id = meta.id
            interface_name = meta.title
            interface_dependency = meta.dependency
            interface_type = "nbproject"

            if interface_name is None:
                raise RuntimeError(
                    "Can only ingest from notebook with title. Please set a title!"
                )
        else:
            interface_dependency = None
            interface_type = "other"

        from lamindb._configuration import user_id, user_name

        df_interface = db.do.load("interface")
        if interface_id not in df_interface.index:
            with sqm.Session(engine) as session:
                # can remove underscore once we explicitly
                # migrate to _id suffixes for id columns
                interface_ = db.model.interface(
                    id=interface_id,
                    name=interface_name,
                    dependency=interface_dependency,
                    type=interface_type,
                    user=user_id,
                )
                session.add(interface_)
                session.commit()
            print(
                f"added interface {interface_name!r} ({interface_id}) by user"
                f" {user_name} ({user_id})"
            )

        with sqm.Session(engine) as session:
            file = db.model.file(name=name, interface=interface_id)
            session.add(file)
            session.commit()
            session.refresh(file)

        return file.id
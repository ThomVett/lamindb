import bionty as bt


class Species(bt.Species):
    """Bionty Species.

    See `bionty.Species <https://lamin.ai/docs/bionty/bionty.Species>`__.
    """

    def __init__(self, id="common_name") -> None:
        super().__init__(id=id)


class Gene(bt.Gene):
    """Bionty Gene.

    See `bionty.Gene <https://lamin.ai/docs/bionty/bionty.Gene>`__.
    """

    def __init__(self, species="human", id="ensembl_gene_id") -> None:
        super().__init__(species=species, id=id)


class Protein(bt.Protein):
    """Bionty Protein.

    See `bionty.Protein <https://lamin.ai/docs/bionty/bionty.Protein>`__.
    """

    def __init__(self, species="human", id="uniprotkb_id") -> None:
        super().__init__(species=species, id=id)


class CellMarker(bt.CellMarker):
    """Bionty CellMarker.

    See `bionty.CellMarker <https://lamin.ai/docs/bionty/bionty.CellMarker>`__.
    """

    def __init__(self, species="human", id="name") -> None:
        super().__init__(species=species, id=id)

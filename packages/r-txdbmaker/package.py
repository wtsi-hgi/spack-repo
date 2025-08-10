from spack.package import *


class RTxdbmaker(RPackage):
    """Make TxDb objects from various annotation resources."""

    bioc = "txdbmaker"

    # Bioconductor DESCRIPTION version
    version("1.5.6", commit="c61f22906e0ed9dcae677d1f0242d14261054d48")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges@1.54.1:", type=("build", "run"))
    depends_on("r-genomicfeatures@1.54.4:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-rsqlite@2.0:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-biomart@2.59.1:", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-ucsc-utils", type=("build", "run"))

    def patch(self):
        # Robustly rewrite DESCRIPTION to match available dependencies
        desc_path = "DESCRIPTION"
        try:
            with open(desc_path, "r", encoding="utf-8") as f:
                s = f.read()
        except FileNotFoundError:
            s = None
        if s is not None:
            s = s.replace("Seq\ninfo", "GenomeInfoDb")
            s = s.replace("Seqinfo", "GenomeInfoDb")
            s = s.replace("GenomicRanges (>= 1.61.1)", "GenomicRanges (>= 1.54.1)")
            s = s.replace("GenomicFeatures (>= 1.61.4)", "GenomicFeatures (>= 1.54.4)")
            with open(desc_path, "w", encoding="utf-8") as f:
                f.write(s)
        # Fix invalid import of non-existent 'Seqinfo' package in NAMESPACE
        ns_path = "NAMESPACE"
        try:
            with open(ns_path, "r", encoding="utf-8") as f:
                ns = f.read()
        except FileNotFoundError:
            ns = None
        if ns is not None:
            ns = ns.replace("import(Seqinfo)", "import(GenomeInfoDb)")
            with open(ns_path, "w", encoding="utf-8") as f:
                f.write(ns)

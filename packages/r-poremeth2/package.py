from spack.package import *


class RPoremeth2(RPackage):
    """PoreMeth2: DMR detection and visualization for Nanopore methylation data.

    Upstream provides an R package with compiled Fortran code and plotting
    utilities. This recipe packages the 1.0 release from GitHub.
    """

    homepage = "https://github.com/Lab-CoMBINE/PoreMeth2"
    url = "https://github.com/Lab-CoMBINE/PoreMeth2/archive/refs/tags/DMRs.tar.gz"
    git = "https://github.com/Lab-CoMBINE/PoreMeth2.git"

    # Upstream release "PoreMeth2 1.0" is tagged as "DMRs"
    version("1.0", sha256="2ad0ee8402db2fd68231cf95dd2b5cb8a5c9341bed0b8961baefcd2ffc110743")

    # Base R dependency; package contains compiled code (Fortran)
    depends_on("r@3.5.0:", type=("build", "run"))


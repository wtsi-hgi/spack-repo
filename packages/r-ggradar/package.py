from spack.package import *


class RGgradar(RPackage):
    """Create radar charts using ggplot2.

    Exposes ggplot2-based functionality to create radar charts. Upstream is a
    GitHub-only R package (no CRAN release).
    """

    homepage = "https://github.com/ricardo-bion/ggradar"
    git = "https://github.com/ricardo-bion/ggradar.git"

    # No tagged releases; track latest commit per repository guidelines
    version("20240223", commit="f99517ae4df2903d3dbd4116af91b24009a5ac93")

    # Runtime/build dependencies from DESCRIPTION (Imports)
    depends_on("r", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))


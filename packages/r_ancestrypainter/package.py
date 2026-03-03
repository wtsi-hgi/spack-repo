from spack.package import *


class RAncestrypainter(RPackage):
    """Visualization of ancestry makeup and genetic difference.

    Based on a simple sector graphing function, this R package can be used
    to visualize the ancestry proportion inferred by population genetics
    software (e.g., ADMIXTURE) and genetic difference (e.g., FST).
    """

    homepage = "https://github.com/Shuhua-Group/AncestryPainterV2"
    url = "https://github.com/Shuhua-Group/AncestryPainterV2/archive/refs/tags/v1.0.tar.gz"
    git = "https://github.com/Shuhua-Group/AncestryPainterV2.git"

    license("GPL-3.0")

    # Upstream provides tags. Use the stable v1.0 tarball.
    version("1.0", sha256="e587413a1f20b34fdc6cf2a263b6902c5961e22d2bb332b971745a8f098a02ee")

    # DESCRIPTION imports only base 'graphics'; no extra R packages needed.
    depends_on("r@3.5.0:", type=("build", "run"))


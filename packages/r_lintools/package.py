from spack.package import *


class RLintools(RPackage):
    """Manipulation of Linear Systems of (in)Equalities.

    Provides tools for Gaussian elimination, Fourier–Motzkin elimination,
    pseudoinverse, reduced row echelon form, projections, simplifications,
    and range computations in linear (in)equation systems.
    """

    cran = "lintools"

    version("0.1.7", sha256="50859bc8eda00450da7afaa7eb041790fa7e666bd0f0bbd299fdd03978e84e0f")

    depends_on("r", type=("build", "run"))

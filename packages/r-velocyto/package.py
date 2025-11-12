# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVelocyto(RPackage):
    """RNA velocity estimation in R.

    Provides routines for estimating gene-specific transcriptional derivatives
    and visualizing the resulting velocity patterns.
    """

    homepage = "https://github.com/velocyto-team/velocyto.R"
    url = "https://github.com/velocyto-team/velocyto.R/archive/refs/tags/0.6.tar.gz"
    git = "https://github.com/velocyto-team/velocyto.R.git"

    license("GPL-3.0-only")

    version("0.6", sha256="3821e86a254bcce844024f7a7e98236f9801f4503143bac5d6c5a4781a438adc")

    # Core R
    depends_on("r", type=("build", "run"))

    # DESCRIPTION: Depends
    depends_on("r-matrix", type=("build", "run"))

    # DESCRIPTION: Imports
    depends_on("r-rcpp@0.12.13:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-pcamethods", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-hdf5r", type=("build", "run"))

    # DESCRIPTION: LinkingTo
    depends_on("r-rcpparmadillo", type=("build", "run"))

    # Native libraries linked in src/Makevars
    depends_on("boost", type=("build", "run"))

    def setup_build_environment(self, env):
        # Ensure Boost libraries are discoverable by the R build/link step
        env.append_flags("LDFLAGS", self.spec["boost"].libs.ld_flags)

    def patch(self):
        # Inject Spack's Boost link flags into Makevars so that the
        # linker sees -L and rpath for Boost libraries.
        boost_ldflags = self.spec["boost"].libs.ld_flags
        filter_file(
            r"^PKG_LIBS=.*$",
            f"PKG_LIBS={boost_ldflags} -lstdc++ $(LAPACK_LIBS) $(BLAS_LIBS)  $(SHLIB_OPENMP_CFLAGS) $(FLIBS)",
            "src/Makevars",
        )

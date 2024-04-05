# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRecommended(BundlePackage):
    "R Packages considered recommended by Conda."

    homepage = "https://anaconda.org/r/r-essentials"

	version("4.2")

    depends_on("r-boot", type=("build", "run"))
    depends_on("r-class", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-codetools", type=("build", "run"))
    depends_on("r-foreign", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-nlme", type=("build", "run"))
    depends_on("r-nnet", type=("build", "run"))
    depends_on("r-rpart", type=("build", "run"))
    depends_on("r-spatial", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClippda(RPackage):
    """A package for the clinical proteomic profiling data analysis

    Methods for the nalysis of data from clinical proteomic profiling studies. The focus is on the studies of human subjects, which are often observational case-control by design and have technical replicates. A method for sample size determination for planning these studies is proposed. It incorporates routines for adjusting for the expected heterogeneities and imbalances in the data and the within-sample replicate correlations.
    """

    homepage = "http://www.cancerstudies.bham.ac.uk/crctu/CLIPPDA.shtml"
    bioc = "clippda"

    version("1.58.0", commit="ee8b6589708ec3219d317650c040c06131289202")
    version("1.52.0", commit="8f0ec8afe32cecb14c04cb29a356bc6a4f81d85e")

    depends_on("r@2.13.1:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))

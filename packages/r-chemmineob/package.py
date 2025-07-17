# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemmineob(RPackage):
    """R interface to a subset of OpenBabel functionalities

    ChemmineOB provides an R interface to a subset of cheminformatics functionalities implemented by the OpelBabel C++ project. OpenBabel is an open source cheminformatics toolbox that includes utilities for structure format interconversions, descriptor calculations, compound similarity searching and more. ChemineOB aims to make a subset of these utilities available from within R. For non-developers, ChemineOB is primarily intended to be used from ChemmineR as an add-on package rather than used directly.
    """

    homepage = "https://github.com/girke-lab/ChemmineOB"
    bioc = "ChemmineOB"
    version("1.46.0", commit="3c9cfd857a4b858afa48a74b612b4532b0281f13")
    version("1.40.0", commit="56dd1da900279e1dc39d9ac5136635b0236ab141")

    depends_on("r@2.15.1:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("openbabel@3.0.0:", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        env.set("OPEN_BABEL_INCDIR", self.spec["openbabel"].prefix.include.openbabel3)
        env.set("OPEN_BABEL_LIBDIR", self.spec["openbabel"].prefix.lib)

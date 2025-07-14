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
	urls = [
	    "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChemmineOB_1.40.0.tar.gz",
	    "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChemmineOB/ChemmineOB_1.40.0.tar.gz",
	]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="b147d9e00df464d13b1c6d876b0a49e158510ff725da599e51b936faf997ca55")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("openbabel@3.0.0:", type=("build", "link", "run"))

	def setup_build_environment(self, env):
	    env.set("OPEN_BABEL_INCDIR", self.spec["openbabel"].prefix.include.openbabel3)
	    env.set("OPEN_BABEL_LIBDIR", self.spec["openbabel"].prefix.lib)

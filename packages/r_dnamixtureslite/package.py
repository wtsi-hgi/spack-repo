# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnamixtureslite(RPackage):
	"""Statistical Inference for Mixed Traces of DNA (Lite-Version)

	Statistical methods for DNA mixture analysis. This package is a lite-version of the 'DNAmixtures' package to allow users without a 'HUGIN' software license to experiment with the statistical methodology. While the lite-version aims to provide the full functionality it is noticeably less efficient than the original 'DNAmixtures' package. For details on implementation and methodology see <https://dnamixtures.r-forge.r-project.org/>.
	"""
	
	cran = "DNAmixturesLite" 

	version("0.0-1", md5="cd938f735092a48fb84faf10b233a6ae")

	depends_on("r-graven", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))

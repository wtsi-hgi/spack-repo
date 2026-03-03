# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabelmixr2(RPackage):
	"""Use 'nlmixr2' to Interact with Open Source and Commercial
Software

	Run other estimation and simulation software via the 'nlmixr2' (Fidler et al (2019)
  <doi:10.1002/psp4.12445>) interface including 'PKNCA', 'NONMEM' and 'Monolix'. While not required, you can
  get/install the 'lixoftConnectors' package in the 'Monolix' installation, as
  described at the following url
  <https://monolix.lixoft.com/monolix-api/lixoftconnectors_installation/>. When
  'lixoftConnectors' is available, 'Monolix' can be run directly instead of setting up
  command line usage.
	"""
	
	homepage = "https://nlmixr2.github.io/babelmixr2/"
	cran = "babelmixr2" 

	version("0.1.2", md5="5d5a55b134bb7e67af6e315c624e8836", url="https://cran.r-project.org/src/contrib/babelmixr2_0.1.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlmixr2@2.0.8:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-nlmixr2est@2.1.6:", type=("build", "run"))
	depends_on("r-nonmem2rx@0.1.3:", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-rxode2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rxode2parse", type=("build", "run"))

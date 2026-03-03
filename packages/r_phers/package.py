# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhers(RPackage):
	"""Calculate Phenotype Risk Scores

	Use phenotype risk scores based on linked clinical and genetic data
  to study Mendelian disease and rare genetic variants. See Bastarache et al.
  2018 <doi:10.1126/science.aal4043>.
	"""
	
	homepage = "https://phers.hugheylab.org"
	cran = "phers" 

	version("1.0.2", md5="ae56a9a7bcf18086a6a36bcf8dacb046")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bedmatrix@2.0.3:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.5:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-iterators@1.0.14:", type=("build", "run"))
	depends_on("r-survival@3.3.1:", type=("build", "run"))

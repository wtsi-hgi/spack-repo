# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzCombat(RPackage):
	"""Easy ComBat Harmonization

	A dataframe-friendly implementation of ComBat Harmonization which uses an empirical Bayesian framework to remove batch effects.
    Johnson WE & Li C (2007)  <doi:10.1093/biostatistics/kxj037> "Adjusting batch effects in microarray expression data using empirical Bayes methods."
    Fortin J-P, Cullen N, Sheline YI, Taylor WD, Aselcioglu I, Cook PA, Adams P, Cooper C, Fava M, McGrath PJ, McInnes M, Phillips ML, Trivedi MH, Weissman MM, & Shinohara RT (2017) <doi:10.1016/j.neuroimage.2017.11.024> "Harmonization of cortical thickness measurements across scanners and sites."
    Fortin J-P, Parker D, Tun<e7> B, Watanabe T, Elliott MA, Ruparel K, Roalf DR, Satterthwaite TD, Gur RC, Gur RE, Schultz RT, Verma R, & Shinohara RT (2017) <doi:10.1016/j.neuroimage.2017.08.047> "Harmonization of multi-site diffusion tensor imaging data."
	"""
	
	cran = "ez.combat" 

	version("1.0.0", md5="9ea6687e6c68472ecc6421cb1d0e2220")

	depends_on("r@3.5:", type=("build", "run"))

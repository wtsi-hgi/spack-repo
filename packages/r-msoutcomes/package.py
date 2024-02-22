# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsoutcomes(RPackage):
	"""CORe Multiple Sclerosis Outcomes Toolkit

	Enable operationalized evaluation of disease outcomes in
    multiple sclerosis.  ‘MSoutcomes’ requires longitudinally recorded
    clinical data structured in long format.  The package is based on the
    research developed at Clinical Outcomes Research unit (CORe),
    University of Melbourne. Lorscheider et al.  (2016)
    <doi:10.1093/brain/aww173>.  Kalincik et al. (2015)
    <doi:10.1093/brain/awv258>.
	"""
	
	cran = "MSoutcomes" 

	version("0.1.0", md5="4846eb1be2b819b80b2ad01d19cc687b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))

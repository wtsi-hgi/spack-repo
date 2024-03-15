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
    University of Melbourne and Neuroimmunology Centre, Royal Melbourne
    Hospital. Kalincik et al. (2015) <doi:10.1093/brain/awv258>.
    Lorscheider et al.  (2016) <doi:10.1093/brain/aww173>. Sharmin et al.
    (2022) <doi:10.1111/ene.15406>.  Dzau et al. (2023)
    <doi:10.1136/jnnp-2023-331748>.
	"""
	
	cran = "MSoutcomes" 

	version("0.2.0", md5="6237d8a510015718a0499016b9175773")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhr(RPackage):
	"""Electronic Health Record (EHR) Data Processing and Analysis Tool

	Process and analyze electronic health record (EHR) data. The 'EHR'
    package provides modules to perform diverse medication-related studies using
    data from EHR databases. Especially, the package includes modules to perform
    pharmacokinetic/pharmacodynamic (PK/PD) analyses using EHRs, as outlined in
    Choi, Beck, McNeer, Weeks, Williams, James, Niu, Abou-Khalil, Birdwell, Roden, 
    Stein, Bejan, Denny, and Van Driest (2020) <doi:10.1002/cpt.1787>. Additional 
    modules will be added in future. In addition, this package provides various 
    functions useful to perform Phenome Wide Association Study (PheWAS) to explore 
    associations between drug exposure and phenotypes obtained from EHR data, as 
    outlined in Choi, Carroll, Beck, Mosley, Roden, Denny, and Van Driest (2018) 
    <doi:10.1093/bioinformatics/bty306>.
	"""
	
	homepage = "https://choileena.github.io/"
	cran = "EHR" 

	version("0.4-11", md5="4df3244dca1317d49c9746922faffad6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pkdata", type=("build", "run"))

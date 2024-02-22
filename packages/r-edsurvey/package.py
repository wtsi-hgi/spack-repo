# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdsurvey(RPackage):
	"""Analysis of NCES Education Survey and Assessment Data

	Read in and analyze functions for education survey and assessment data from the National Center for Education Statistics (NCES) <https://nces.ed.gov/>, including National Assessment of Educational Progress (NAEP) data <https://nces.ed.gov/nationsreportcard/> and data from the International Assessment Database: Organisation for Economic Co-operation and Development (OECD) <https://www.oecd.org/>, including Programme for International Student Assessment (PISA), Teaching and Learning International Survey (TALIS), Programme for the International Assessment of Adult Competencies (PIAAC), and International Association for the Evaluation of Educational Achievement (IEA) <https://www.iea.nl/>, including Trends in International Mathematics and Science Study (TIMSS), TIMSS Advanced, Progress in International Reading Literacy Study (PIRLS), International Civic and Citizenship Study (ICCS), International Computer and Information Literacy Study (ICILS), and Civic Education Study (CivEd).
	"""
	
	homepage = "https://www.air.org/project/nces-data-r-project-edsurvey"
	cran = "EdSurvey" 

	version("4.0.4", md5="5b85ffad98583540041adb4adb32c472")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-car@3.1.2:", type=("build", "run"))
	depends_on("r-lfactors@1.0.3:", type=("build", "run"))
	depends_on("r-dire@2.2:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-haven@2.2:", type=("build", "run"))
	depends_on("r-laf@0.8.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.6.1.1:", type=("build", "run"))
	depends_on("r-naepprimer@1.0.1:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-wcorr@1.9.8:", type=("build", "run"))
	depends_on("r-naepirtparams@1:", type=("build", "run"))
	depends_on("r-wemix@4:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))

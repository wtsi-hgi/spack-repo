# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsmprep(RPackage):
	"""Data Preparation During and After the Use of the Experience
Sampling Methodology (ESM)

	Support in preparing a raw ESM dataset for statistical analysis. Preparation includes the handling of errors (mostly due to technological reasons) and the generating of new variables that are necessary and/or helpful in meeting the conditions when statistically analyzing ESM data. The functions in 'esmprep' are meant to hierarchically lead from bottom, i.e. the raw (separated) ESM dataset(s), to top, i.e. a single ESM dataset ready for statistical analysis. This hierarchy evolved out of my personal experience in working with ESM data.
	"""
	
	homepage = "https://github.com/mmiche/esmprep"
	cran = "esmprep" 

	version("0.2.0", md5="49aed697646ad89ac669c875c738c5e6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtnote(RPackage):
	"""CTN Outcomes, Treatments, and Endpoints

	The Clinical Trials Network (CTN) of the U.S. National Institute
  of Drug Abuse sponsored the CTN-0094 research team to harmonize data sets
  from three nationally-representative clinical trials for opioid use disorder
  (OUD). The CTN-0094 team herein provides a coded collection of trial outcomes
  and endpoints used in various OUD clinical trials over the past 50 years.
  These coded outcome functions are used to contrast and cluster different
  clinical outcome functions based on daily or weekly patient urine screenings.
  Note that we abbreviate urine drug screen as "UDS" and urine opioid screen as
  "UOS". For the example data sets (based on clinical trials data harmonized by
  the CTN-0094 research team), UDS and UOS are largely interchangeable.
	"""
	
	homepage = "https://ctn-0094.github.io/CTNote/"
	cran = "CTNote" 

	version("0.1.0", md5="ecd77a9b7bc901cf6a9defe21135ca07")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

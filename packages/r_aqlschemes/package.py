# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAqlschemes(RPackage):
	"""Retrieving Acceptance Sampling Schemes

	Functions are included for recalling AQL (Acceptable Quality Level or Acceptance Quality Level) 
 Based single, double, and multiple attribute sampling plans from the Military Standard (MIL-STD-105E) - American 
 National Standards Institute/American Society for Quality (ANSI/ASQ Z1.4) tables and for retrieving variable
 sampling plans from Military Standard (MIL-STD-414) - American National Standards Institute/American Society
 for Quality (ANSI/ASQ Z1.9) tables. The sources for these tables are listed in the URL: field. Also included
 are functions for computing the OC (Operating Characteristic) and ASN (Average Sample Number) coordinates
 for the attribute plans it recalls, and functions for computing the estimated proportion nonconforming and
 the maximum allowable proportion nonconforming for variable sampling plans. The MIL-STD AQL Sampling schemes
 were the most used and copied set of standards in the world. They are intended to be used for sampling a stream
 of lots, and were used in contract agreements between supplier and customer companies. When the US military
 dropped support of MIL-STD 105E and 414, The American National Standards Institute (ANSI) and the International
 Standards Organization (ISO) adopted the standard with few changes or no changes to the central tables. This
 package is useful because its computer implementation of these tables duplicates that available in other
 commercial software and subscription online calculators. 
	"""
	
	homepage = "https://archive.org/details/MIL-STD-105E_1"
	cran = "AQLSchemes" 

	version("1.7-2", md5="8e3f42b6772a71619e40010dbe0cc3f2")


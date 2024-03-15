# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetsearchdata(RPackage):
	"""Example GC-MS data for TargetSearch Package

	Example files of GC-MS data for the TargetSearch Package. The package contains raw NetCDF files from a E.coli salt stress experiment, extracted peak lists, and sample metadata required for a GC-MS analysis. The raw data has been restricted for demonstration purposes.
	"""
	
	homepage = "https://github.com/acinostroza/TargetSearchData"
	bioc = "TargetSearchData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TargetSearchData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TargetSearchData/TargetSearchData_1.40.0.tar.gz"]

	version("1.40.0", md5="96bbec70706d8adcf4ee321261620d79")


	# experiment
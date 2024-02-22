# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJoinxl(RPackage):
	"""Perform Joins or Minus Queries on 'Excel' Files

	Performs Joins and Minus Queries on 'Excel' Files
    fulljoinXL() Merges all rows of 2 'Excel' files based upon a common column in the files.
    innerjoinXL() Merges all rows from base file and join file when the join condition is met.
    leftjoinXL() Merges all rows from the base file, and all rows from the join file
    if the join condition is met.
    rightjoinXL() Merges all rows from the join file, and all rows from the base file if the join
    condition is met.
    minusXL() Performs 2 operations source-minus-target and target-minus-source
    If the files are identical all output files will be empty.
    Choose two 'Excel' files via a dialog box, and then follow prompts at the console to
    choose a base or source file and columns to merge or minus on.
	"""
	
	homepage = "http://github.com/yvonneglanville/joinXL"
	cran = "joinXL" 

	version("1.0.1", md5="0e6448801d7b0becffa6c948adb5ca1b")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-readxl@0.1.1:", type=("build", "run"))
	depends_on("r-openxlsx@3:", type=("build", "run"))
	depends_on("r-timeseries@3022.101.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rchoicedialogs@1.0.6:", type=("build", "run"))
	depends_on("r-r-utils@2.3:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("r-rcpp@0.11.1:", type=("build", "run"))
	depends_on("r-timedate@2150.95:", type=("build", "run"))

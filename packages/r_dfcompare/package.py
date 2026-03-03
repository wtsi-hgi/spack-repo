# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfcompare(RPackage):
	"""Compare Two Dataframes and Return Adds, Changes, and Deletes

	Compares two dataframes with a common key
            and returns the delta records. The package will return
            three dataframes that contain the added, changed,
            and deleted records.
	"""
	
	homepage = "https://github.com/swaldroff/DFCompare"
	cran = "dfCompare" 

	version("1.0.0", md5="a53339a93085aaca540843438d2a3d33")


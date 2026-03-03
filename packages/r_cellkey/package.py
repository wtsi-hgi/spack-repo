# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellkey(RPackage):
	"""Consistent Perturbation of Statistical Frequency- And Magnitude
Tables

	Data from statistical agencies and other institutions often
    need to be protected before they can be published. This package 
    can be used to perturb statistical tables in a consistent way. The
    main idea is to add - at the micro data level - a record key for each
    unit. Based on these keys, for any cell in a statistical table a
    cell key is computed as a function on the record keys contributing to
    a specific cell. Values that are added to the cell in order to perturb
    it are derived from a lookup-table that maps values of cell keys to 
    specific perturbation values. The theoretical basis for the methods 
    implemented can be found in Thompson, Broadfoot and Elazar 
    (2013) <https://unece.org/fileadmin/DAM/stats/documents/ece/ces/ge.46/2013/Topic_1_ABS.pdf>
    which was extended and enhanced by Giessing and Tent 
    (2019) <https://unece.org/fileadmin/DAM/stats/documents/ece/ces/ge.46/2019/mtg1/SDC2019_S2_Germany_Giessing_Tent_AD.pdf>.
	"""
	
	homepage = "https://github.com/sdcTools/cellKey"
	cran = "cellKey" 

	version("1.0.2", md5="d7034345d8b33aa7dab4e0b0522e92f8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-sdchierarchies@0.19.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-digest@0.6.23:", type=("build", "run"))
	depends_on("r-sdctable@0.32.2:", type=("build", "run"))
	depends_on("r-ptable@1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))

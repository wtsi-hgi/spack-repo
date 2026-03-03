# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwig(RPackage):
	"""Half-Weight Index Gregariousness

	The half-weight index gregariousness (HWIG) is an association 
             index used in social network analyses. It extends the half-weight 
             association index (HWI), correcting for level of gregariousness 
             in individuals. It is calculated using group by individual 
             data according to methods described in Godde et al. (2013) 
             <doi:10.1016/j.anbehav.2012.12.010>. 
	"""
	
	homepage = "https://gitlab.com/robit.a/hwig"
	cran = "hwig" 

	version("0.0.2", md5="66a168e4eaaf4b4ce2c45af30dd4708f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-asnipe", type=("build", "run"))
	depends_on("r-spatsoc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaditr(RPackage):
	"""Fast Data Aggregation, Modification, and Filtering with Pipes
and 'data.table'

	Provides pipe-style interface for 'data.table'. Package preserves all 'data.table' features without
              significant impact on performance. 'let' and 'take' functions are simplified interfaces for most common data
              manipulation tasks. For example, you can write 'take(mtcars, mean(mpg), by = am)' for aggregation or 
              'let(mtcars, hp_wt = hp/wt, hp_wt_mpg = hp_wt/mpg)' for modification. Use 'take_if/let_if' for conditional
              aggregation/modification. Additionally there are some conveniences such as automatic 'data.frame' 
              conversion to 'data.table'.
	"""
	
	homepage = "https://github.com/gdemin/maditr"
	cran = "maditr" 

	version("0.8.4", md5="0bb8dff0baa9b22ea2f56db774ffe430")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))

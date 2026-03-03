# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemindr(RPackage):
	"""Insert and Extract "Reminders" from Function Comments

	Insert/extract text "reminders" into/from function source code 
    comments or as the "comment" attribute of any object.  
    The former can be handy in development as reminders of e.g. argument
    requirements, expected objects in the calling environment, required options
    settings, etc. The latter can be used to provide information of the object and 
    as simple manual "tooltips" for users, among other things.
	"""
	
	cran = "remindR" 

	version("0.0.1", md5="40cbdda2db0e10a201fce760e02f7482")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))

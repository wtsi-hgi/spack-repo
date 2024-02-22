# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMailr(RPackage):
	"""A Utility to Send Emails from R

	Interface to Apache Commons Email to send emails
    from R.
	"""
	
	homepage = "https://github.com/rpremrajGit/mailR"
	cran = "mailR" 

	version("0.8", md5="e48b032cf87f404176a128c059138573")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))

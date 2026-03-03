# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjmgr(RPackage):
	"""Task Tracking and Project Management with GitHub

	Provides programmatic access to 'GitHub' API with a
    focus on project management.  Key functionality includes
    setting up issues and milestones from R objects or 'YAML' configurations,
    querying outstanding or completed tasks, and generating progress updates
    in tables, charts, and RMarkdown reports. Useful for those using 'GitHub' in personal,
    professional, or academic settings with an emphasis on streamlining
    the workflow of data analysis projects.
	"""
	
	homepage = "https://github.com/emilyriederer/projmgr"
	cran = "projmgr" 

	version("0.1.1", md5="c7ad974d36f11288e3af5453f65af77a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

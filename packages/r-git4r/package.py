# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGit4r(RPackage):
	"""Interactive Git for R

	An interactive git user interface from the R command line. Intuitive
         tools to make commits, branches, remotes, and diffs an integrated part
         of R coding. Built on git2r, a system installation of git is not required
         and has default on-premises remote option.
	"""
	
	homepage = "https://github.com/johnxhobbs/git4r"
	cran = "git4r" 

	version("0.1.2", md5="4bfe7c6772f65188b5463302eaae464c")

	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-diffr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGit2rdata(RPackage):
	"""Store and Retrieve Data.frames in a Git Repository

	The git2rdata package is an R package for writing and reading
    dataframes as plain text files.  A metadata file stores important
    information.  1) Storing metadata allows to maintain the classes of
    variables.  By default, git2rdata optimizes the data for file storage.
    The optimization is most effective on data containing factors.  The
    optimization makes the data less human readable.  The user can turn
    this off when they prefer a human readable format over smaller files.
    Details on the implementation are available in vignette("plain_text",
    package = "git2rdata").  2) Storing metadata also allows smaller row
    based diffs between two consecutive commits.  This is a useful feature
    when storing data as plain text files under version control.  Details
    on this part of the implementation are available in
    vignette("version_control", package = "git2rdata").  Although we
    envisioned git2rdata with a git workflow in mind, you can use it in
    combination with other version control systems like subversion or
    mercurial.  3) git2rdata is a useful tool in a reproducible and
    traceable workflow.  vignette("workflow", package = "git2rdata") gives
    a toy example.  4) vignette("efficiency", package = "git2rdata")
    provides some insight into the efficiency of file storage, git
    repository size and speed for writing and reading.
	"""
	
	homepage = "https://ropensci.github.io/git2rdata/"
	cran = "git2rdata" 

	version("0.4.0", md5="40e81100082c57dd33f46b6fdc7fa056")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-git2r@0.23:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))

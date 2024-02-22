# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrompt(RPackage):
	"""Dynamic 'R' Prompt

	Set the 'R' prompt dynamically, from a function. The package
    contains some examples to include various useful dynamic information
    in the prompt: the status of the last command (success or failure);
    the amount of memory allocated by the current 'R' process; the name of
    the R package(s) loaded by 'pkgload' and/or 'devtools'; various 'git'
    information: the name of the active branch, whether it is dirty,
    if it needs pushes pulls. You can also create your own prompt if you
    don't like the predefined examples.
	"""
	
	homepage = "https://github.com/gaborcsardi/prompt"
	cran = "prompt" 

	version("1.0.2", md5="fee1b4477ab38a90e7ba29989bcdc2ee")

	depends_on("r-cli", type=("build", "run"))

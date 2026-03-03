# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepigner(RPackage):
	"""A Utility Package to Help you Deal with "Pignas"

	Pigna [_pìn'n'a_] is the Italian word for pine cone.  In
    jargon, it is used to identify a task which is boring, banal,
    annoying, painful, frustrating and maybe even with a not so beautiful
    or rewarding result, just like the obstinate act of trying to
    challenge yourself in extracting pine nuts from a pine cone, provided
    that, in the end, you will find at least one inside it. Here you can
    find a backpack of functions to be used to solve small everyday
    problems of coding or analyzing (clinical) data, which would be
    normally solved using quick-and-dirty patches. You will be able to
    convert 'Hmisc' and 'rms' summary()es into data.frames ready to be
    rendered by 'pander' and 'knitr'. You can access easy-to-use wrappers
    to activate essential but useful progress bars (from 'progress') into
    your loops or functionals. Easy setup and control Telegram's bots
    (from 'telegram.bot') to send messages or to divert error messages to
    a Telegram's chat. You also have some utilities helping you in the
    development of packages, like the activation of the same user
    interface of 'usethis' into your package, or call polite functions to
    ask a user to install other packages. Finally, you find a set of
    thematic sets of packages you may use to set up new environments
    quickly, installing them in a single call.
	"""
	
	homepage = "https://corradolanera.github.io/depigner/"
	cran = "depigner" 

	version("0.9.1", md5="637652f80e830f3e45c7b8052b9122d7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-hmisc@4.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.2.2:", type=("build", "run"))
	depends_on("r-rms@5.1.2:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-telegram-bot@2.3:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-usethis@1.5:", type=("build", "run"))

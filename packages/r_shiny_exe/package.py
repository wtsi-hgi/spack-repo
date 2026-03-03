# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyExe(RPackage):
	"""Launch a Shiny Application without Opening R or RStudio

	Launch an application by a simple click without opening R or RStudio. The package has 3 functions of which only one is essential in its use, `shiny.exe()`. It generates a script in the open shiny project then create a shortcut in the same folder that allows you to launch the app by clicking.If you set `host = 'public'`, the application will be launched on the public server to which you are connected. Thus, all other devices connected to the same server will be able to access the application through the link of your `IPv4` extended by the port. You can stop the application by leaving the terminal opened by the shortcut.
	"""
	
	homepage = "https://github.com/AODiakite"
	cran = "shiny.exe" 

	version("0.2.0", md5="4439125c5941ae3cb587a337c6e55210")


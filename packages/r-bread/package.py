# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBread(RPackage):
	"""Analyze Big Files Without Loading Them in Memory

	A simple set of wrapper functions for data.table::fread() that allows subsetting or
    filtering rows and selecting columns of table-formatted files too large for the available RAM.
    'b stands for 'big files'.
    bread makes heavy use of Unix commands like 'grep', 'sed', 'wc', 'awk' and 'cut'. They are available 
    by default in all Unix environments.
    For Windows, you need to install those commands externally in order to simulate a 
    Unix environment and make sure that the executables are in the Windows PATH variable.
    To my knowledge, the simplest ways are to install 'RTools', 'Git' or 'Cygwin'. If they have been 
    correctly installed (with the expected registry entries), they should be detected on loading
    the package and the correct directories will be added automatically to the PATH.
	"""
	
	homepage = "https://github.com/MagicHead99/bread/"
	cran = "bread" 

	version("0.4.1", md5="c973a5515a6364533a26d52586f8e557")

	depends_on("r-data-table", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStv(RPackage):
	"""Single Transferable Vote Counting

	Implementations of the Single Transferable Vote counting 
    system. By default, it uses the Cambridge method for surplus allocation
    and Droop method for quota calculation.  Fractional surplus allocation
    and the Hare quota are available as options.
	"""
	
	homepage = "https://github.com/jayemerson/STV"
	cran = "STV" 

	version("1.0.2", md5="fcd8b6bc4cba97e63b4e0b9d856e4e56")


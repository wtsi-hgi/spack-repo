# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeypress(RPackage):
	"""Wait for a Key Press in a Terminal

	Wait for a single key press at the 'R' prompt.
    This works in terminals, but does not currently work
    in the 'Windows' 'GUI', the 'OS X' 'GUI' ('R.app'),
    in 'Emacs' 'ESS', in an 'Emacs' shell buffer or in
    'R Studio'. In these cases 'keypress' stops with an
    error message.
	"""
	
	homepage = "https://github.com/gaborcsardi/keypress#readme"
	cran = "keypress" 

	version("1.3.1", md5="75986d5cf49909b4b4e4d9143c5a699e")


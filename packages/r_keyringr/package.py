# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyringr(RPackage):
	"""Decrypt Passwords from Gnome Keyring, Windows Data Protection
API and macOS Keychain

	Decrypts passwords stored in the Gnome Keyring, macOS Keychain and
    strings encrypted with the Windows Data Protection API.
	"""
	
	cran = "keyringr" 

	version("0.4.0", md5="3a2a49e86c8126e7309c77ebd529aafd")

	depends_on("r-stringr", type=("build", "run"))

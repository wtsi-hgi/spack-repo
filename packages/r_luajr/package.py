# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLuajr(RPackage):
	"""'LuaJIT' Scripting

	An interface to 'LuaJIT' <https://luajit.org>, a just-in-time 
    compiler for the 'Lua' scripting language <https://www.lua.org>. Allows 
    users to run 'Lua' code from 'R'.
	"""
	
	homepage = "https://github.com/nicholasdavies/luajr"
	cran = "luajr" 

	version("0.1.6", md5="252d1c4ab0fe0c182101f03a3ca51ade")


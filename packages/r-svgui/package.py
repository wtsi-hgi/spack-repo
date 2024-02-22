# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvgui(RPackage):
	"""SciViews - Manage GUIs in R

	The 'SciViews' 'svGUI' package eases the management of Graphical
  User Interfaces (GUI) in R. It is independent from any particular GUI widgets
  ('Tk', 'Gtk2', native, ...). It centralizes info about GUI elements currently
  used, and it dispatches GUI calls to the particular toolkits in use in
  function of the context (is R run at the terminal, within a 'Tk' application,
  a HTML page?).
	"""
	
	homepage = "https://github.com/SciViews/svGUI"
	cran = "svGUI" 

	version("1.0.1", md5="1f6b7f275fda2066db762a0d1791ec56")

	depends_on("r@2.6:", type=("build", "run"))

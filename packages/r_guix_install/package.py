# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuixInstall(RPackage):
	"""Install R Packages with GNU Guix

	This 'R' package provides a single procedure guix.install(),
  which allows users to install 'R' packages via 'Guix' right from within
  their running 'R' session.  If the requested 'R' package does not exist
  in 'Guix' at this time, the package and all its missing dependencies
  will be imported recursively and the generated package definitions
  will be written to ~/.Rguix/packages.scm.  This record of imported
  packages can be used later to reproduce the environment, and to add
  the packages in question to a proper 'Guix' channel (or 'Guix' itself).
  guix.install() not only supports installing packages from CRAN, but
  also from Bioconductor or even arbitrary 'git' or 'mercurial'
  repositories, replacing the need for installation via 'devtools'.
	"""
	
	homepage = "https://github.com/BIMSBbioinfo/guix.install"
	cran = "guix.install" 

	version("1.0.0", md5="dfce3a087cbb9f7874106a38fd07bb6d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcwb(RPackage):
	"""'Rcpp' Bindings for the 'Corpus Workbench' ('CWB')

	'Rcpp' Bindings for the C code of the 'Corpus Workbench' ('CWB'), an indexing and query 
  engine to efficiently analyze large corpora (<https://cwb.sourceforge.io>). 'RcppCWB' is licensed
  under the GNU GPL-3, in line with the GPL-3 license of the 'CWB' (<https://www.r-project.org/Licenses/GPL-3>).
  The 'CWB' relies on 'pcre2' (BSD license, see <http://www.pcre.org/licence.txt>)
  and 'GLib' (LGPL license, see <https://www.gnu.org/licenses/lgpl-3.0.en.html>).
  See the file LICENSE.note for further information. The package includes modified code of the
  'rcqp' package (GPL-2, see <https://cran.r-project.org/package=rcqp>). The original work of the authors
  of the 'rcqp' package is acknowledged with great respect, and they are listed as authors of this
  package. To achieve cross-platform portability (including Windows), using 'Rcpp' for wrapper code
  is the approach used by 'RcppCWB'.
	"""
	
	homepage = "https://github.com/PolMine/RcppCWB"
	cran = "RcppCWB" 

	version("0.6.4", md5="99c43a734b0c35f29f0f1d41c5e163af")
	version("0.6.3", md5="1690c8855973bac06a8e3b87fc409e41")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("pcre2", type=("build", "link", "run"))
	depends_on("glib@2.0.0:", type=("build", "link", "run"))

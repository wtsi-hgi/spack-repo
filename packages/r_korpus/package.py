# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKorpus(RPackage):
	"""Text Analysis with Emphasis on POS Tagging, Readability, and
Lexical Diversity

	A set of tools to analyze texts. Includes, amongst others, functions for
          automatic language detection, hyphenation, several indices of lexical diversity
          (e.g., type token ratio, HD-D/vocd-D, MTLD) and readability (e.g., Flesch,
          SMOG, LIX, Dale-Chall). Basic import functions for language corpora are also
          provided, to enable frequency analyses (supports Celex and Leipzig Corpora
          Collection file formats) and measures like tf-idf. Note: For full functionality
          a local installation of TreeTagger is recommended. It is also recommended to
          not load this package directly, but by loading one of the available language
          support packages from the 'l10n' repository
          <https://undocumeantit.github.io/repos/l10n/>. 'koRpus' also includes a plugin
          for the R GUI and IDE RKWard, providing graphical dialogs for its basic
          features. The respective R package 'rkward' cannot be installed directly from a
          repository, as it is a part of RKWard. To make full use of this feature, please
          install RKWard from <https://rkward.kde.org> (plugins are detected
          automatically). Due to some restrictions on CRAN, the full package sources are
          only available from the project homepage. To ask for help, report bugs, request
          features, or discuss the development of the package, please subscribe to the
          koRpus-dev mailing list (<https://korpusml.reaktanz.de>).
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=koRpus"
	cran = "koRpus" 

	version("0.13-8", md5="87f5cf19ee31e22af6e8f099290440d8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sylly@0.1.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

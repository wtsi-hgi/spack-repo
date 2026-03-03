# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsa(RPackage):
    """Multiple Sequence Alignment

    The 'msa' package provides a unified R/Bioconductor interface to the multiple sequence alignment algorithms ClustalW, ClustalOmega, and Muscle. All three algorithms are integrated in the package, therefore, they do not depend on any external software tools and are available for all major platforms. The multiple sequence alignment algorithms are complemented by a function for pretty-printing multiple sequence alignments using the LaTeX package TeXshade.
    """

    homepage = "http://www.bioinf.jku.at/software/msa/"
    bioc = "msa"
    # Prefer a responsive Bioconductor mirror first; keep upstream/Archive as fallbacks
    urls = [
        "https://bioconductor.statistik.tu-dortmund.de/packages/3.18/bioc/src/contrib/msa_1.34.0.tar.gz",
        "https://bioconductor.riken.jp/packages/3.18/bioc/src/contrib/msa_1.34.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/msa/msa_1.34.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/msa_1.34.0.tar.gz",
    ]

    version("1.34.0", md5="78eba41452ffe497e1a7c72116335b3e")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biostrings@2.40:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-iranges@1.20:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

    def patch(self):
        filter_file(
            """#include <pthread.h>""",
            """#define _GNU_SOURCE 1
#include <pthread.h>""",
            "src/gc-8.2.2/configure",
            string=True,
        )
        
        # Fix C++ standard conflict in ClustalOmega Makefile
        filter_file(
            """-std=c++98""",
            """-std=c++11""",
            "src/ClustalOmega/msaMakefile",
            string=True,
        )
        
        # Fix isnan/isinf namespace issues in hhalign code
        filter_file(
            """isnan(""",
            """std::isnan(""",
            "src/ClustalOmega/src/hhalign/hhhit-C.h",
            string=True,
        )
        filter_file(
            """isinf(""",
            """std::isinf(""",
            "src/ClustalOmega/src/hhalign/hhhit-C.h",
            string=True,
        )
        filter_file(
            """isnan(""",
            """std::isnan(""",
            "src/ClustalOmega/src/hhalign/hhalign.cpp",
            string=True,
        )

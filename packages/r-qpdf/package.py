# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RQpdf(RPackage):
    """Content-preserving transformations transformations of PDF files such as split, combine, and compress."""

    homepage = "https://www.example.com"
    cran = "qpdf"

    version("1.3.2", sha256="d9c905a4879274d72de0c638f2e14737ec0a59895cbba9814e05c62b43e8e976")
    version("1.3.1", sha256="600c6ba670f691794611b1fc1486160d55ca2fdfa6bbc737cbe6db4073c59c5c")
    version("1.3.0", sha256="c8a9ecf05b6fe41c1a521d6cf290c9fc4a6cee502045f359b8a0daadc84a5674")
    version("1.2.0", sha256="d03db36a2024e8db3792f96b5c694578a5ccd36b86c58a0cf82451d1d43f2da8")
    version("1.1", sha256="71f106925aeffcf3cae500aad5f9306b64a9ed963540ec1d77a161c49975960e")
    version("1.0", sha256="3c7f0c0ce4822f67e477d970f0d04659ca0ef9a11cb070df3e338c2346bd5622")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-askpass", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))

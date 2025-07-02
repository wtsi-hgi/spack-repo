# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RCmdstanr(RPackage):
    """R Interface to 'CmdStan'.

    A lightweight interface to 'Stan' <https://mc-stan.org>.  The 'CmdStanR'
    interface is an alternative to 'RStan' that calls the command line
    interface for compilation and running algorithms instead of interfacing
    with C++ via 'Rcpp'. This has many benefits including always being
    compatible with the latest version of Stan, fewer installation errors,
    fewer unexpected crashes in RStudio, and a more permissive license."""

    homepage = "https://mc-stan.org/cmdstanr/"
    url = "https://github.com/stan-dev/cmdstanr/archive/refs/tags/v0.5.3.tar.gz"

    license("BSD-3-Clause")

    version("0.9.0", sha256="55e1d9f7d2dba08771850243944606020c9ca4e682ff53ab6a4e9fbc3032a003")
    version("0.8.1", sha256="d151ad183a9aa340bd444ccf3e75e133f0ce4cb9502a917b98406f4f593209f5")
    version("0.8.0", sha256="cf59fbed7163dcee55533d5394809414717b281c27414ec7374e360458f8e31a")
    version("0.7.1", sha256="62e552c641c4faaf64edaf0951a8c39dde8758193154bb79c6b7df114bce233c")
    version("0.7.0", sha256="5310e31516b4ef782c5828a35757927f6ec71b7ded7456c9cc6ff4677b368a49")
    version("0.6.1", sha256="493972deb6a915918e2f24a55b7c9f67c7c140bcd103239716318fb1283a5ee2")
    version("0.6.0", sha256="e3f9612dee592b2dff7592d779c4d449dbb2b94e1aa8348a032e784fae3d753d")
    version("0.5.3", sha256="dafd5808e1a17d2e4ae4048437235b4399464a7c65de68ba4af0ab2b03e27871")
    version("0.5.2", sha256="5bc2e164e7cce3bfb93d592df5e3059157c8d510b136535bdb6d09c3ef060f64")
    version("0.5.1", sha256="5b3e83d48c19d309ccca720979449a8ac130ba7e443e70992b1771a1dd9124c9")

    depends_on("r@3.5.0:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-jsonlite@1.2.0:", type=("build", "run"))
    depends_on("r-posterior@1.1.0:", type=("build", "run"))
    depends_on("r-processx@3.5.0:", type=("build", "run"))
    depends_on("r-r6@2.4.0:", type=("build", "run"))
    depends_on("r-withr@2.5.0:", type=("build", "run"), when="@0.5.2:")
    depends_on("cmdstan", type="run")

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install genotyping
#
# You can edit this file again by typing:
#
#     spack edit genotyping
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path
import tempfile


class Genotyping(PerlPackage):
    """Components of the WTSI genotype analysis pipeline.

    This is the perl Genotyping module, a component of the WTSI genotype
    analysis pipeline which provides command-line applications. These
    applications may be run manually or within a pipeline defined by the
    Ruby Genotyping module."""

    homepage = "https://github.com/wtsi-npg/genotyping/tree/devel"
    url = "https://github.com/wtsi-npg/genotyping/archive/refs/tags/1.14.3.tar.gz"

    version("1.14.3", sha256="f4969cb6519902a3b569073b3067542b5822e3211a449eff346d3a528cd70be3")
    version("1.14.2", sha256="013436582e70e590d0b91dd0ca6f187f18070c28c5c8516edba94dbc16d29e67")
    version("1.14.1", sha256="a94fd85ed2bbfe4ed3acebb06e2c038163027d97f77f7fe249cd2a36103aabd3")
    version("1.14.0", sha256="7d01d50b0dfdf1652e484d522699744cf66c9d918e30fa866800f8ac4296256c")
    version("1.13.2", sha256="78412d0303c1bdbc31e580235c3c5e1ca3d4f3e1ea49ad2032729d68f8bbc9b0")
    version("1.13.1", sha256="893ba0048b08db57f85dc2d425ee9dc8c1f4994a05ed7b88cab7750e38aa261f")
    version("1.13.0", sha256="ff87bf3a6ca2970cdec07c1823a5d75bebe82792047bf4ecca41f084543b4960")
    version("1.12.0", sha256="da209c32919fb72c93aa9d0f3c73d02f291e50caef33e99e3448dac602ea0c22")

    depends_on("perl-module-build", type="build")
    depends_on("perl-list-allutils", type="build")
    depends_on("perl-dnap-utilities", type="build")

    def patch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            move("src/perl", temp_dir)
            move("src/r", temp_dir)
            for i in Path(".").iterdir():
                try:
                    remove(i)
                except OSError:
                    rmtree(i)
            for i in Path(temp_dir, "perl").iterdir():
                move(i, ".")
            move(Path(temp_dir, "r"), ".")
        filter_file("../r", "r", "Build.PL", string=True)

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
#     spack install girara
#
# You can edit this file again by typing:
#
#     spack edit girara
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Girara(MesonPackage):
    """Girara is a library that implements a user interface
    that focuses on simplicity and minimalism. It is designed
    to replace and enhance the user interface used by zathura."""

    homepage = "https://pwmt.org/projects/girara"
    url = "https://github.com/pwmt/girara/archive/refs/tags/0.4.5.tar.gz"
    git = "https://github.com/pwmt/girara.git"

    # Maintainers should be the Spack maintainers responsible for this package
    # Replace with actual maintainers if submitting as a PR
    maintainers("github_user1", "github_user2")

    license("Zlib")

    version("0.4.5", sha256="9abb84fdb3f8f51e8aef8d53488fd0631357f0713ad5aa4a5c755c23f54b23df")
    version("0.4.4", sha256="4e25b0e58317dc12c3d466b28d798cd60ad65b2db17e28685e32dd4cab54361b")
    version("0.4.3", sha256="89c1c57d5a6dc81b7683f8529e89ac33d94ab43b20a79b0a3195c5eb5099eecb")

    # Required dependencies
    depends_on("gtkplus@3.24:", type=("build", "run", "link"))
    depends_on("glib@2.72:", type=("build", "run", "link"))

    # Build dependencies
    depends_on("meson@0.61:", type="build")
    depends_on("gettext", type="build")
    depends_on("pkgconfig", type="build")

    # Optional dependencies
    variant("json", default=True, description="Enable json-glib support for configuration dumping")
    variant("docs", default=False, description="Build HTML documentation")

    depends_on("json-glib", when="+json", type=("build", "run", "link"))
    depends_on("doxygen", when="+docs", type="build")

    def meson_args(self):
        args = []

        if "+json" in self.spec:
            args.append("-Djson=enabled")
        else:
            args.append("-Djson=disabled")

        if "+docs" in self.spec:
            args.append("-Ddocs=enabled")
        else:
            args.append("-Ddocs=disabled")

        return args

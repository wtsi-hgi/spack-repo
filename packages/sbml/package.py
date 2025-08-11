from spack.package import *


class Sbml(CMakePackage):
    """LibSBML is a library for reading, writing, and manipulating SBML files.

    This local recipe ensures that libxml2 include and library paths are passed
    explicitly to CMake for reliable builds across environments.
    """

    homepage = "https://sbml.org/Software/libSBML/"
    url = "https://github.com/sbmlteam/libsbml/archive/refs/tags/v5.18.0.tar.gz"
    git = "https://github.com/sbmlteam/libsbml.git"

    license("LGPL-2.1-or-later")

    # Versions (keep 5.18.0 for requested spec and newer tags for completeness)
    version("5.20.5", sha256="21c88c753a4a031f157a033de3810488b86f003e684c6ca7aa3d6e26e7e0acfc")
    version("5.20.4", sha256="02c225d3513e1f5d6e3c0168456f568e67f006eddaab82f09b4bdf0d53d2050e")
    version("5.20.2", sha256="a196cab964b0b41164d4118ef20523696510bbfd264a029df00091305a1af540")
    version("5.20.1", sha256="4463d44b55b9c05eb45248fee44b0b1391c1a563947b8d28894a426fd0df1dc9")
    version("5.20.0", sha256="400f1e1039ef0fc9addc99660a3a2559fefe9cb2c8315b1b488014b6101c438f")
    version("5.19.7", sha256="61cbdf1a86aefbc002ac5a0cf9c0f3f91eca2ae8aa5c3e7ef78be0f5a84426c5")
    version("5.19.6", sha256="77990b0f7b7419269061fbe671540c10f87f52bf8a8568953675ee615584efa6")
    version("5.19.5", sha256="6c0ec766e76bc6ad0c8626f3d208b4d9e826b36c816dff0c55e228206c82cb36")
    version("5.19.2", sha256="5b4d7a34e3d516877525041334ee9bcdd79a3dd6334d9e1a61e0687ed9751e78")
    version("5.19.0", sha256="127a44cc8352f998943bb0b91aaf4961604662541b701c993e0efd9bece5dfa8")
    version("5.18.0", sha256="6c01be2306ec0c9656b59cb082eb7b90176c39506dd0f912b02e08298a553360")

    # Core dependencies
    depends_on("cmake@3.16:", type="build")
    depends_on("zlib")
    depends_on("bzip2")
    depends_on("libxml2")

    def cmake_args(self):
        libxml2_spec = self.spec["libxml2"]

        # Use the canonical include directory containing libxml/parser.h
        libxml_include_dir = join_path(libxml2_spec.prefix.include, "libxml2")

        # Determine the absolute path to the libxml2 library
        libxml_library_path = libxml2_spec.libs[0]

        args = [
            # Ensure XML backend selection and compression libs
            self.define("WITH_LIBXML", True),
            self.define("WITH_XERCES", False),
            self.define("WITH_EXPAT", False),
            self.define("WITH_ZLIB", True),
            self.define("WITH_BZIP2", True),

            # Pass explicit libxml2 locations to avoid auto-detection pitfalls
            self.define("LIBXML_INCLUDE_DIR", libxml_include_dir),
            self.define("LIBXML_LIBRARY", libxml_library_path),

            # Keep build lean (language bindings and extras off)
            self.define("WITH_SWIG", False),
            self.define("WITH_EXAMPLES", False),
            self.define("WITH_TESTS", False),
            self.define("WITH_CHECK", False),
            self.define("WITH_PYTHON", False),
            self.define("WITH_JAVA", False),
            self.define("WITH_CSHARP", False),
            self.define("WITH_R", False),
            self.define("WITH_PERL", False),
        ]
        return args


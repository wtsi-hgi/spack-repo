from spack.package import *


class PyEzdxf(PythonPackage):
    """A Python package to create/manipulate DXF drawings."""
    
    homepage = "https://ezdxf.mozman.at"
    pypi = "ezdxf/ezdxf-1.4.2b1-py3-none-any.whl" 

    version(
        "1.4.2b1",
        sha256="df1561c054ba8b47208545cb4d48bbecab34fd9833c7c46fc3bd756ef6091669",
        expand=False,
        url="https://files.pythonhosted.org/packages/bc/dc/015484badf1b374727f79ad13c39b888fa51d7efad72dbf0f30eb9b3d710/ezdxf-1.4.2b1-py3-none-any.whl",
    )

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-typing-extensions@4.6:", type=("build", "run"))
    depends_on("py-pyparsing@2.0.1:", type=("build", "run"))
    depends_on("py-fonttools", type=("build", "run"))


/*
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * See end of file for extended copyright information
 */

// Include header files
#include <iostream>
#include "../header/{{ projectName }}.h"

// Preprocessor macro
#define Log(x) (std::cout << x << std::endl)

{{ projectName.capitalize() }}::{{ projectName.capitalize() }}()
{
    Log("{{ projectName.capitalize() }} created");
}

{{ projectName.capitalize() }}::~{{ projectName.capitalize() }}()
{
    Log("{{ projectName.capitalize() }} destroyed");
}

/*
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * 
 * {{ projectName }}
 * {{ projectDescription }}
 *
{% if licenseName == "All Rights Reserved" %} * All Rights Reserved{% else %}
 * This code is licensed under the {{ licenseName }}.
 * Please see the LICENSE file in the root directory of this project for the full license details.{% endif %}
 */

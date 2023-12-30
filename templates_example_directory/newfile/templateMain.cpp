/*
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * See end of file for extended copyright information
 */

// Include header files
#include <iostream>

// Preprocessor macro
#define Log(x) (std::cout << x << std::endl)

int main(int argc, char* argv[])
{
    // Write code here
    Log("{{ projectName }} created");

    // End program
    return 0;
}

/*
 * Copyright (C) {{ year }} {{ projectAuthor }}
 * 
 * {{ projectName }}
 * {{ projectDescription }}
 *
 * {% if licenseName == "All Rights Reserved" %}All Rights Reserved{% else %}This code is licensed under the {{ licenseName }}.
 * Please see the LICENSE file in the root directory of this project for the full license details.{% endif %}
 */

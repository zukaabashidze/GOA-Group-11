const names = ['zuka', 'zuka', 'zuka']
export default function app(){
    return(
        <main>
            <ol>
            {names.map((name)=>(

                <li>{name}</li>
            ))}

            </ol>


        </main>
    )
}